# Exit if we have an error
set -e
# Check for 5 parameters
if [ $# -ne 5 ]
then
        echo "5 Arguments expected"
        exit 1
fi
# set params
script_dir=$1
db_user=$2
db_host=$3
db_name=$4
db_pass=$5
# Check scripts path exists
if [[ ! -d "$script_dir" ]]
then
        echo "Scripts path $script_dir does not exist"
fi
# Check if we can login to sql server
mysql -h $db_host -u $db_user -p$db_pass -se"USE $db_name;"
# Get list of files in scripts order by number sequence ascending
for sql in `ls -v $script_dir`
do
        # For each file check if order number greater than sql version
        db_ver=`mysql -s -N -e "select version from $db_name.versionTable"`
        sql_ver=$(echo $sql | sed -e 's/[^0-9]//g')
        # Apply SQL code if true
        if [ "$sql_ver" -gt "$db_ver" ]; then
                echo "Applying $sql"
                mysql -h $db_host -u $db_user -p$db_pass $db_name < $script_dir/$sql
                mysql -h $db_host -u $db_user -p$db_pass $db_name -e "update $db_name.versionTable SET version=$sql_ver"
        else
                echo "Skipping $sql"
        fi
done