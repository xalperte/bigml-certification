#!/usr/bin/env python
# -*- coding: utf-8 -*
import os
from bigml.api import BigML

API = BigML(debug=False)

OUTPUT_FOLDER = 'question_2a_1'


def main():
    """Question 2.A
    """

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    with open('question_1b_1/dataset_gen', 'r') as f:
        train_dataset_id = f.readline().strip()

    print "Using training set: [%s]" % train_dataset_id

    with open('question_1a/dataset_test', 'r') as f:
        test_dataset_id = f.readline().strip()

    print "Using test set: [%s]" % test_dataset_id

    model = API.create_model(origin_resource=train_dataset_id, args={
        'stat_pruning': True, 'seed': 'bigmler',
        'name': 'Diabetes Analysis',
        'tags': [
            'BigML Certification', 'Advanced API 2',
            'Question 2', 'Question 2 - Part 1']
    })

    print "Waiting until the model is created..."
    API.ok(model)

    print "Model ID: [%s]" % model['resource']
    with open('%s/model' % OUTPUT_FOLDER, 'w+') as f:
        f.write(model['resource'])

    evaluation = API.create_evaluation(
        model, test_dataset_id, args={
            'name': 'Diabetes Analysis',
            'tags': [
                'BigML Certification', 'Advanced API 2',
                'Question 2', 'Question 2 - Part 1']
        })
    print "Waiting until the evaluation is created..."
    API.ok(evaluation)

    print "Evaluation ID: [%s]" % evaluation['resource']
    with open('%s/evaluation' % OUTPUT_FOLDER, 'w+') as f:
        f.write(evaluation['resource'])

if __name__ == "__main__":
    main()
