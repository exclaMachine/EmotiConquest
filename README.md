# EmotiConquest

png emoji images are from https://github.com/googlefonts/noto-emoji/
Used the following git commands to filter only the 72 px images

git filter-branch --subdirectory-filter png/72 -- --all

rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now

word list is from
https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b
