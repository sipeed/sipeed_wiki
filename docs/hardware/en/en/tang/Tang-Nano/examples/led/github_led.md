# Blink by github project

- First get sourcecode from github https://github.com/sipeed/Tang-Nano-examples
  
- Open led_prj.gprj file in Tang-Nano-examples\example_led\led_prj path
- Right click clean&Rerun all in process interface
  ![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/github_place&route.png)

- Then there is an error(This is a historical question,  you can search it by yourself if you wonder it)
  Change configuration which can be found in  Project -> Configuration -> Syntheize of top menu bar and choose GowinSyntheize.
  Then right click Place&Route and  clean&Rerun all 
   ![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/Change_Synthesis.png)

- Connet the board and download firmware.
  Double click `Program Device` in Process interface to open programmer tool.
  ![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/Open_Programmer.png)

- Choose download to SRAM to verify codes quickly
  ![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/Success_led.png)

<p id="back">
    <a href="#" onClick="javascript :history.back(-1);">返回上一页(Back)</a>
</p>