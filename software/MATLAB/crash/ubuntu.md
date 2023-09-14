

Working with ubuntu 20.04, MATLAB crashes when opening Simulink. To solve the issue, run the following in the terminal:

```
open_system(new_system('abcdef123456')); bdclose('abcdef123456')
```