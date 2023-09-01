
class Point:
  def __init__(self,x,y):
    self.x=x
    self.y=y
    def program_input(no_of_traps):
      point_list = []
      x_coordinates = []
      y_coordinates = []
      for i in range(no_of_traps):
        x,y = [float(i) for i in input().split()]
        y_coordinates.append(y)
        x_coordinates.append(x)
        point_list.append(Point(x,y))
        poly_vertices = convex_hull((point_list),len(point_list)) 
        return
        poly_vertices,x_coordinates,y_coordinates

        def convex_hull(point_list,no_of_traps) -> [int] :
          if no_of_traps < 3:
            return
          bottomost_point = left_index(point_list)
          hull=[]
          first_point = bottomost_point
          second_point = 0
          while(True):
          hull.append(first_point)
          second_point = (first_point + 1)% no_of_traps
          for i in range(no_of_traps):
              if orientation(point_list[first_point],point_list[i],point_list[second_point]) == 2):
                second_point = i
                first_point = second_point
                if(first_point == bottomost_point):
                  break
                  vertices = []
                  start_vertex = []
                  for each_trap in hull:
                    vertices.append([point_list[each_trap].x,point_list[each_trap].y])
                    start_vertex.append(vertices[0])
                    vertices.extend(start_vertex)
                    return vertices[::-1]  

            def left_index(point_list):
              minimum = 0
              for i in range(1,len(point_list)):
                if point_list[i].y< point_list[minimum].y:
                  minimum = i
                  elif point_list[i].y == point_list[minimum].y:
                    if point_list[i].x < point_list[minimum].x:
                      minimum = i
              return minimum

                      def orientation(first_point, second_point, third_point):
                        value = ((second_point.y - first_point.y) * (third_point.x - second_point.x)) - ((second_point.x - first_point.x) * (third_point.y - second_point.y))
                        if value == 0:
                          return 0 # collinear
                        elif value > 0:
                          return 1 # Clockwise
                        else:
                          return 2 # Counterclockwise

                              import math
                              def perimeter_length(point_list)  ->  int :
                                  perimeter = 0
                                  for i in range(0,len(point_list))  :
                                      point_1 = point_list[i]
                                      if i == len(point_list) - 1 :
                                           break
                                      else  :
                                           point_2 = point_list[i+1]
                                      perimeter += math.sqrt(((point_2[0]-point_1[0])**2)+((point_2[1]-point_1[1])**2))
                                 return round(perimeter,2)   


               def program_output(point_list)  -> str :
                 list1 = []
                 final_list = []
                 for i in(tuple(coordinate) for coordinate in point_list):
                   list1.append(i)
                   tuple_form = tuple(list1)
                   for i in tuple_form:
                     s=str(i)
                     final_list.append(s)
                     poly_edges = "-".join(final_list)
                     print(poly_edges)

                     import matplotlib.pyplot as plt
                     def program_plot(x,y,point_list):
                       plt.scatter(x,y,color = 'black')
                       plt.xlabel("X - Axis")
                       plt.xlabel("Y - Axis")
                       x_points = []
                       y_points = []
                       points = [point for coordinate in point_list for point in coordinate]
                       x_points = points[::2]
                       y_points = points[1::2]
                       plt.plot(x_points,y_points,color='green')
                       plt.legend(["Outline","Moth Trap Location"],loc = "upper right")
                       plt.show()


                        no_of_traps=1
                       while(no_of_traps!=0) :
                         for region in range(1,1000):
                           no_of_traps = int(input())
                           if (no_of_traps == 0):
                             break
                             poly_vertices,x_points,y_points = program_input(no_of_traps)
                             print()
                             print("Region #",region,":")
                             program_output(poly_vertices)
                             print("Perimeter Length = ",perimeter_length(poly_vertices))
                             program_plot(x_points,y_points,poly_vertices)
                     

