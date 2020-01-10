git add . && git filter-branch -f --msg-filter 'sed "s/^/bug ###### - /"' master..HEAD && git commit
