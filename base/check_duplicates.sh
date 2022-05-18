
#Checks if two submissions are identical
#Run in submissions directory

OUTPUTFILE=duplicates.txt

for first in *; do
    if [ -d "${first}" ]; then 
	#rm -rf "${first}/allsrc"
	unzip -o "${first}/allsrc.zip" -d "${first}/allsrc"
    fi
done

rm ${OUTPUTFILE}

for first in *; do
    for second in *; do
	if [ -d "${first}" ] && [ -d "${second}" ] && [ "${first}" != "${second}" ]; then 
	    if [ -d "${first}/allsrc" ] && [ -d "${second}/allsrc" ]; then 
		diffidx=$(diff -r "${first}/allsrc" "${second}/allsrc" | wc -c)
		if test ${diffidx} -lt 10; then
		    echo ${first} ${second} ${diffidx} >> ${OUTPUTFILE}
		fi
	    fi
	fi
    done
done

wc -l ${OUTPUTFILE}
