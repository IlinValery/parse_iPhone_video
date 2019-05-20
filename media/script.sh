for file in *.MOV
do
  filename="${file%.*}"
  mkdir "$filename"
  mv "$file" "$filename"
done
