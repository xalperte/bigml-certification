#!/bin/sh

bigmler --train s3://bigml-public/csv/diabetes.csv --test-split 0.2 --name "Diabetes Analysis" --tag "BigML Certification" --tag "Advanced API 2" --tag "Question 1" --seed bigmler --output-dir question_1a --evaluate
