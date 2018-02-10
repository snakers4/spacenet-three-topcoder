python3 train_satellites.py \
--arch linknet34 --batch-size 1 \
--imsize 1280 --preset mul_ps_vegetation --augs True \
--workers 6 --epochs 40 --start-epoch 0 \
--seed 42 --print-freq 20 \
--lr 1e-3 --optimizer adam \
--tensorboard True --lognumber test \
--params /data/AOI_2_Vegas_Roads_Train
