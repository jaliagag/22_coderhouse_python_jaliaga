```bash
git fetch --all
git reset --hard origin/master
git pull origin/master
#
git pull --rebase --autostash
# overwrite local changes
git reset --hard origin/master
git pull
# keep local changes
git stash
git pull
git stash pop
```
