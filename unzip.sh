for filename in *.tar.gz
do
  tar -xvzf $filename
  rm $filename
done
