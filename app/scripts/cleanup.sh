#!/bin/bash
set -e

echo "Cleaning old app directory..."
rm -rf /var/www/app
mkdir -p /var/www/app