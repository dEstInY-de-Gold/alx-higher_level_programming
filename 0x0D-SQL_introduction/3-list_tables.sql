#!/usr/bin/env bash

# Get the database name as an argument.
database_name="$1"

# Run the MySQL command to list tables.
mysql -e "USE $database_name; SHOW TABLES;"
