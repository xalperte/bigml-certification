#!/bin/sh

#bigmler anomaly --dataset `cat question_1a/dataset_train` --name "Diabetes Analysis" --tag "BigML Certification" --tag "Advanced API 2" --tag "Question 1b" --seed bigmler --anomaly-seed bigmler --top-n 2 --score --remote --anomalies-dataset out --output-dir question_1b_1

bigmler --dataset `cat question_1b_1/dataset_gen` --test-dataset `cat question_1a/dataset_test` --name "Diabetes Analysis" --tag "BigML Certification" --tag "Advanced API 2" --tag "Question 1b" --seed bigmler --output-dir question_1b_2 --evaluate
