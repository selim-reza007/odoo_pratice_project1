{
    'name': 'School system',
    'author': 'Selim Reza',
    'website' : 'hslbd.onrender.com',
    'version' : '1.0.0',
    'category' : 'Informal',
    'summary' : 'Some dummy sumarry',
    'description' : 'Some dummy description info',
    'application' : True,
    'depends' : ["mail"],
    'data' : [
          'views/menu.xml',
          'views/student.xml',
          'views/teacher.xml',
          'security/ir.model.access.csv',
    ],
    'sequence' : -1,
}