# EmotiConquest

png emoji images are from https://github.com/googlefonts/noto-emoji/
Used the followoing git commands to filter only the 72 px images

git filter-branch --subdirectory-filter png/72 -- --all

rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now
