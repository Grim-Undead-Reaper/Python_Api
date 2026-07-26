ListOfRoutes = []

ListOfRoutes.append({"url":"/", "description": "Homepage", "statusCode":[200, 400], "methodsAllowed":["GET", "POST"]})
ListOfRoutes.append({"url":"/api/add/<name>", "description": "Save and show the name in url.", "statusCode":[200, 400], "methodsAllowed":["GET", "POST"]})
ListOfRoutes.append({"url":"/api/update/<oldname>/<newname>", "description": "Update a old username.", "statusCode":[200, 400], "methodsAllowed":["GET", "POST"]})
ListOfRoutes.append({"url":"/api/delete/<name>", "description": "Delete selected user.", "statusCode":[200, 400], "methodsAllowed":["GET", "POST"]})
ListOfRoutes.append({"url":"/api/search/<name>", "description": "Search for a user.", "statusCode":[200, 400], "methodsAllowed":["GET", "POST"]})
ListOfRoutes.append({"url":"/api/routes", "description": "how all routes and his description.", "statusCode":[200, 400], "methodsAllowed":["GET", "POST"]})
ListOfRoutes.append({"url":"/auth/register", "description": "Register user page.", "statusCode":[200, 400], "methodsAllowed":["GET", "POST"]})
ListOfRoutes.append({"url":"/auth/login", "description": "Make user login.", "statusCode":[200, 400], "methodsAllowed":["GET", "POST"]})