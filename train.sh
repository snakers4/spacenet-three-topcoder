mkdir -p wdata && \
printf '\nWdata folder created\n' && \
sleep 3 && \
python3 copy_files.py --params $* && \
sleep 3 && \
python3 create_binary_masks.py --params $* && \
sleep 3 && \
python3 extract_metadata.py --params $* && \
sleep 3 && \
cd src && \
echo 'python3 train_satellites.py \
--arch linknet34 --batch-size 6 \
--imsize 1280 --preset mul_ps_vegetation --augs True \
--workers 6 --epochs 40 --start-epoch 0 \
--seed 42 --print-freq 20 \
--lr 1e-3 --optimizer adam \
--tensorboard True --lognumber ln34_mul_ps_vegetation_aug_dice \
--params '$* > train.sh && \
sh train.sh
cd ../ && \
rm -rf wdata && \
printf '\nWdata folder deleted\n' && \ 
sleep 3
