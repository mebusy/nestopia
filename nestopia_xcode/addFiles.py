import os

if __name__ == '__main__':
    from mod_pbxproj import XcodeProject
    # open the project
    project = XcodeProject.Load('nestopia_xcode.xcodeproj/project.pbxproj')

    with open( "./cpp.txt" ) as fp:
        lines = fp.readlines()

    for line in lines:
        line = "../" + line.strip()
        
        _path, _file = os.path.split( line )
        _filename2, _ext = os.path.splitext( _file )

        _filename = _filename2.replace( "nestopia-" , "" )

        # print _path
        for ext in [ ".cpp", ".hpp", ".inl"] :
            dist = os.path.join( _path, _filename + ext  )
            # print dist
            if os.path.exists( dist ) :
                # print dist
                # project.remove_file_by_path( dist )
                group = project.get_or_create_group( _path[3:] )
                project.add_file_if_doesnt_exist( dist, parent = group )
                pass

    # save the project, otherwise your changes won't be picked up by Xcode
    project.save()


