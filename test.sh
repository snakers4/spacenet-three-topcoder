mkdir -p wdata && \
printf '\nWdata folder created\n' && \
sleep 3 && \
python3 copy_files_test.py --params $* && \
sleep 3 && \
python3 create_8bit_test_images.py --params  $* && \
sleep 3 && \
python3 extract_metadata_test.py --params  $* && \
sleep 3 && \
cd src && \
echo 'python3 train_satellites.py \
--arch linknet34 --batch-size 4 \
--imsize 1312 --preset mul_ps_vegetation --augs True \
--workers 6 --epochs 50 --start-epoch 0 \
--seed 42 --print-freq 10 \
--lr 1e-3 --optimizer adam \
--lognumber norm_ln34_mul_ps_vegetation_aug_dice_predict \
--predict --resume weights/norm_ln34_mul_ps_vegetation_aug_dice_best.pth.tar \
--params '$* > predict.sh && \
sh predict.sh # && \
python3 final_model_lstrs.py --folder norm_ln34_mul_ps_vegetation_aug_dice_predict --params $* && \
cd ../ && \
rm -rf wdata && \ 
printf '\nWdata folder deleted\n' && \ 
sleep 3