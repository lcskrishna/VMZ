python3.6 tools/train_net.py \
--train_data=/data/datasets/ResNext3D/ucf101_train01 \
--test_data=/data/datasets/ResNext3D/ucf101_test01 \
--model_name=ir-csn --model_depth=152 \
--clip_length_rgb=4 --batch_size=4 \
--db_type='pickle' \
--jitter_scale="112,112" \
--gpus=0 --base_learning_rate=0.0025 \
--epoch_size=100000 --num_epochs=45 --step_epoch=10 \
--weight_decay=0.005 --num_labels=101 --use_local_file=0

