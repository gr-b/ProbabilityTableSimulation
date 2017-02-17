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
Prob: 0.624 | Samples: 1000 | Non-rejected: 1000
SD: 0.4843800161030593 | Error: +/-0.061269764158188175
(0.593365117920906,0.654634882079094)

Expected Prob: 0.624, Our prob (rounded): 0.624, CORRECT


## 1 test case other nodes
>> python3.6 sample.py cloudy=false 1000
Prob: 0.07573244886677723 | Samples: 50000 | Non-rejected: 5427
SD: 0.26456954672716626 | Error: +/-0.004732763930066006
(0.07336606690174423,0.07809883083181023)

Expected Prob: 0.0756, Our prob (rounded): 0.0756 CORRECT

## 3 other nodes in between

>> python3.6 sample.py snow=true 20000 cloudy=true temperature=cold exams=false
Prob: 0.47522464698331196 | Samples: 20000 | Non-rejected: 3895
SD: 0.4993858046469668 | Error: +/-0.014124763555766829
(0.46816226520542853,0.4822870287611954)

Expected Prob: 0.4719, Our prob (rounded): 0.471 CORRECT

## Additional test case

ddeisadze$ python3.6 sample.py humidity=low 1000 humidity=high
Prob: 0.0 | Samples: 1000 | Non-rejected: 321
SD: 0.0 | Error: +/-0.0
(0.0,0.0)

We already know that this probably would be 0. CORRECT