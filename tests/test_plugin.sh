#! /bin/bash
set -e

curdir=${0%/*}
res_topdir=${curdir:?}/res/

# .. seealso: tox.ini
[[ -n "${IN_TOXENV:-}" ]] || {
        echo "[Error] $0 expects to run in tox environment!"
        exit -1
}

prep () {
        python3 setup.py bdist_wheel
        pip3 install $(ls -1t ${curdir}/../dist/*.whl | head -n 1)
}

prep

# test cases should succeed.
for resdir in ${res_topdir}/*/ok; do
    for yml in ${resdir}/*.yml; do 
      yamllint -c ${resdir}/dot.yamllint ${yml}
    done
done

# test cases should fail.
for resdir in ${res_topdir}/*/ng; do
    for yml in ${resdir}/*.yml; do 
      yamllint -c ${resdir}/dot.yamllint ${yml} && false || :
    done
done
