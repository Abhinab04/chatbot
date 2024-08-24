#!/bin/bash
pip install waitress
waitress-serve --port=$PORT flask_try:app
