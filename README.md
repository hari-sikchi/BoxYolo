# Yolo in Caffe


## Instructions

### Prepare data (In this case VOCdevkit)(http://host.robots.ox.ac.uk/pascal/VOC/voc2007/index.html)

  cd data/yolo
  ln -s /your/path/to/VOCdevkit/ .
  [You can also get the data at (https://drive.google.com/drive/folders/0B4JSh9t8oHVmQ09rd3dPYlJOX0U?usp=sharing). Copy this in data/yolo/]
  python ./get_list.py
  [change related paths in script convert.sh]
  ./convert.sh 


### Training

  cd examples/yolo
  Have a look at the train nets available(Googlenet,ZG,VGG16) and write the name of net you want to use for yolo in gnet_solver
  [change related paths in script train.sh]
  mkdir models
  ./train.sh 


### Testing

  cd examples/yolo
  ./test.sh model_path gpu_id
 

### Reference

 You Only Look Once: Unified, Real-Time Object detection(http://arxiv.org/abs/1506.02640)
