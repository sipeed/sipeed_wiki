---
title: self learning classifier
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: self learning classifier
---


No need to train separately, learn the object features directly on the development board, and then use it directly

Demo video: [youtube](https://www.youtube.com/watch?v=aLW1YQrT-2A) or [bilibili](https://www.bilibili.com/video/BV1Ck4y1d7tx)

## Instructions

* [Here](https://dl.sipeed.com/MAIX/MaixPy/release/master/maixpy_v0.5.0_33_gfcd6d8a) Download version >= v0.5.0-33 firmware
* [Download kmodel](https://maixhub.com/modelInfo?modelId=16)
* Use [kflash_gui](https://github.com/sipeed/kflash_gui) to download firmware and model
* Run [Sample script](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/self_learning_classifier/self_learning_classifier.py)
> If use the lite version kmodel, you should add `fea_len` arg as `512` when create classifier object, when use the bigger kmodel this param is not needed:
```python
classifier = kpu.classifier(model, class_num, sample_num, fea_len=512)
```

Then start learning objects after running

* Press the `boot button` on the development board to capture 3 categories `mobile`, `car`, `keyboard`, each category only needs to be captured once
* Then capture 15 pictures, no order is required, such as capturing 5 pictures of `mobile phone`, 5 `cars`, 5 pictures of `keyboard`
* Then it will automatically learn the features of these 15 pictures
* The last recognized image category will be displayed in the upper left corner



## Save/load learned features

* Use `classifier.save(path)` to save the learned features to the `path` file
* Use `KPU.classifier.load()` to load features, refer to [self_learning_classifier_load.py](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/self_learning_classifier/self_learning_classifier_load.py) file
