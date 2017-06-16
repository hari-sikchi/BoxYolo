import inception_v4


def save_proto(proto, prototxt):
    with open(prototxt, 'w') as f:
        f.write(str(proto))


if __name__ == '__main__':
    model = inception_v4.InceptionV4('imagenet_test_lmdb', 'imagenet_train_lmdb', 1000)

    train_proto = model.inception_v4_proto(64)
    test_proto = model.inception_v4_proto(64, phase='TEST')

    save_proto(train_proto, 'imagenet_train.prototxt')
    save_proto(test_proto, 'imagenet_test.prototxt')
