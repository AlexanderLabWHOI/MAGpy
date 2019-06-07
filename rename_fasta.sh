for x in $(ls mags/*fa);
do 
    name=${x//\./-}
    mv $x ${name/-fa/.fa}
done
