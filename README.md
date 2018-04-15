# pyevm : python ethereum virtual machine

## Running

1. create a `virtualenv` environment

```
pip install virtualenv
```
or if using `conda`
```
conda install virtualenv
```

2. Create virtual env, start it & check if everything's fine
```
virtualenv /path/to/project
source /path/to/project/bin/activate
echo $VIRTUAL_ENV
```

3. Install required packages from requirements.txt
```
pip install -r requirements.txt
```

## Testing pyevm
```
py.test tests
```

## References

**Ethereum py-evm**

https://github.com/ethereum/py-evm/

**Logs and events**

https://media.consensys.net/technical-introduction-to-events-and-logs-in-ethereum-a074d65dd61e
