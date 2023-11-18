#!/usr/bin/fish

# Define the path to your models directory
set models_dir ./models

# Function to replace a symbolic link with the file it points to
function replace_symlink_with_file
    set link_target (readlink $argv[1])

    # Check if the link target is a relative path
    if test -f $models_dir/$link_target
        echo "Copying $link_target to replace symbolic link $argv[1]"
        cp $models_dir/$link_target $argv[1]

        # Remove the symbolic link
        echo "Removing symbolic link $argv[1]"
        rm $argv[1]
    else
        echo "The link target $link_target for $argv[1] is not a file or not in the expected directory."
    end
end

# Iterate over all symbolic links in the models directory
for link in (find $models_dir -type l)
    replace_symlink_with_file $link
end

echo "Symbolic link replacement complete."
