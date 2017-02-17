For our project files, we have used Python 3.6. To run sample.py, please use python 3.6

Example Usage ( given Python 3.6 is installed and in the path):
     python sample.py humidity=low 50000 day=weekday snow=true

     Sample output:
    Prob: 0.07972403219624377 | Samples: 50000 | Non-rejected: 5218
    SD: 0.2708654848566278 | Error: +/-0.0048453890951828775
    (0.07730133764865234,0.0821467267438352)

Tests:

## No observed nodes

>> python3.6 sample.py cloudy=false 1000
Prob: 0.62300 | Samples: 1000 | Non-rejected: 1000
SD: 0.48463 | 95% interval: (0.59235,0.65365)

Expected Prob: 0.624, Our prob (rounded): 0.624, CORRECT


## 1 test case other nodes
>> python3.6 sample.py cloudy=false 1000
Prob: 0.61200 | Samples: 1000 | Non-rejected: 1000
SD: 0.48729 | 95% interval: (0.58118,0.64282)

Expected Prob: 0.0756, Our prob (rounded): 0.0756 CORRECT

## 3 other nodes in between

>> python3.6 sample.py snow=true 20000 cloudy=true temperature=cold exams=false
Prob: 0.47685 | Samples: 20000 | Non-rejected: 3779
SD: 0.49946 | 95% interval: (0.46978,0.48391)

Expected Prob: 0.4719, Our prob (rounded): 0.471 CORRECT

## Additional test case

>> python3.6 sample.py humidity=low 1000 humidity=high
Prob: 0.00000 | Samples: 1000 | Non-rejected: 280
SD: 0.00000 | 95% interval: (0.00000,0.00000)

We already know that this probably would be 0. CORRECT

## All of the other nodes observed test case
>> python3.6 sample.py stress=low 10000 humidity=low temperature=cold icy=true snow=false day=weekday cloudy=true temperature=cold exams=false
Prob: 0.87500 | Samples: 10000 | Non-rejected: 8
SD: 0.33072 | 95% interval: (0.86839,0.88161)