#SCRIPT FOR READING SEQUENCES NAMES FROM RAD DATA FOLDER
#This loop iterates through the raw data folder and outputs soft links to fasta files

cd /proj/uppstore2017185/b2014034/private/raw_data/Vanessa/Vcardui_RAD/RAD_DEMULTIPLEXED/
for filename in * ; do
	echo "$filename"
done
