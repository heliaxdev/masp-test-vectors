#!/usr/bin/env bash

tv_scripts=(
    f4jumble_long
    f4jumble
    orchard_empty_roots
    orchard_generators
    orchard_group_hash
    orchard_key_components
    orchard_map_to_curve
    orchard_merkle_tree
    orchard_note_encryption
    orchard_poseidon_hash
    orchard_poseidon
    orchard_sinsemilla
    sapling_generators
    sapling_key_components
    sapling_note_encryption
    sapling_signatures
    sapling_zip32)

for generator in "${tv_scripts[@]}"
do
    echo "# $generator"
    poetry run python ./$generator.py -t $1 >test-vectors/$1/$generator.$2
done
