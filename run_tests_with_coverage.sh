#!/usr/bin/env bash
coverage erase
coverage run manage.py test --settings=wedish.settings.test
coverage report