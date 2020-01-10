#
#kk="git log --source"
#eval $kk
#store_number=$kk
daynTime=$( date '+%F_%H:%M:%S' )

git add . && git commit -am \"${dayntine}\" && git push
