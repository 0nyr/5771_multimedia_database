from graphviz import Digraph

dot = Digraph(comment='Zoo Database', format='png')

# Entities with their attributes as table rows
dot.node('A', '''<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
    <TR><TD><B>Animals</B></TD></TR>
    <TR><TD>
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR><TD>Name</TD></TR>
            <TR><TD>Gender</TD></TR>
            <TR><TD>Type</TD></TR>
            <TR><TD>Age</TD></TR>
            <TR><TD>Image</TD></TR>
        </TABLE>
    </TD></TR></TABLE>>''')

dot.node('K', '''<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
    <TR><TD><B>Keepers</B></TD></TR>
    <TR><TD>
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR><TD>Name</TD></TR>
            <TR><TD>Pass-photo</TD></TR>
        </TABLE>
    </TD></TR></TABLE>>''')

dot.node('C', '''<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
    <TR><TD><B>Cages</B></TD></TR>
    <TR><TD>
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR><TD>Pitch</TD></TR>
        </TABLE>
    </TD></TR></TABLE>>''')

# Relationships with cardinalities
dot.edge('A', 'C', headlabel='1', taillabel='1', labeldistance='2.5', labelangle='45', fontsize='20')
dot.edge('C', 'K', headlabel='1..*', taillabel='*', labeldistance='2.5', labelangle='-45', fontsize='20')

# Save the output
dot.render('zoo_database.gv', view=True)
