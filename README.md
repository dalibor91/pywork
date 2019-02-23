# pywork

Spawning just one worker
```
python run.py subcmd --run "--target dosleep --seconds 10"
```

in this case worker will be called as follows
```
python run.py subcmd --target dosleep --seconds 10
```

To spawn process and redirect output to file
```
python run.py subcmd --run "--target dosleep --seconds 10" --output log/test
```

Spawning 10 workers with output to /dev/null
```
python run.py subcmd --worker "--target dosleep --seconds 10" --number 10 --noout
```

in this case workes will be spawned with following command
```
python run.py subcmd --target dosleep --seconds 10 --worker_id [0-9]
```
