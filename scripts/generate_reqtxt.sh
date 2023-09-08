poetry export --without-hashes --format=requirements.txt > requirements.txt
sed 's/\;.*$//g' requirements.txt > temp.txt 
mv temp.txt requirements.txt