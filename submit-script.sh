snakemake   \
            --jobs 100 -s MAGpy --use-conda --profile tara-metag  \
                     --cluster-config MAGpy.yaml --cluster "sbatch --parsable --qos=unlim --partition={cluster.queue} --job-name=MAGpy.{rule} --mem={cluster.mem}gb --time={cluster.time} --ntasks={cluster.threads} --nodes={cluster.nodes}"

