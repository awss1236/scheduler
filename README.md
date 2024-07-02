# Scheduler
Top 10 most uncreative names.
Just generates possible schedules based on the times available,
the things to take the aforementioned times
and custom constraints.
## Usage
### Running
Just
```
python main.py
```
lol.
### Available times
The set of available times is auto generated for now.
One can set it manually by changing `awkat`.
### The things (find a better name for this)
It is also hard-coded for now. But, you should be able to change it
(by changing `mawad`) all you want as the names are completely arbitrary (unless when it
comes to the constraints).
### The constraints
The constraints are handled by the `selection` function that receives
a schedule mid-generation and a candidat for a certain time spot.
It must return a boolean. If it returns true, then the candidat is
deamed acceptable and the generation continues with another.
Otherwise, it drops the candidat for another.
