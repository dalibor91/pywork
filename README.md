# pywork

Spawning just one worker
```
python run.py subcmd --run "--dosleep 15"
```

in this case worker will be called as follows
```
python run.py subcmd --dosleep 15
```

Spawning 10 workers
```
python run.py subcmd --worker "--dosleep 15" --number 10
```

in this case workes will be spawned with following command
```
python run.py subcmd --dosleep 15 --worker_id [0-9]
```
