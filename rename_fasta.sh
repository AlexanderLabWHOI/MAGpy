for x in $(mags/*fa);
do 
    name=${x//\./-}
    mv $x ${name/-fa/.fa}
done
