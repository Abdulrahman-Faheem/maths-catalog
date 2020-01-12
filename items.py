from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Categories, Items


#engine = create_engine('sqlite:///itemcatalog.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create a user
user1 = User(name = "admin", email = "abdulrahmanfaheem776@gmail.com")
session.add(user1)
session.commit()

# Menu for Algebra
category1 = Categories(name = "Algebra")
session.add(category1)
session.commit()


item1 = Items(
        name = "Algebra 1 or Elementary Algebra",
        description = "Elementary Algebra covers the traditional topics studied in a modern elementary algebra course.\
            Arithmetic includes numbers along with mathematical operations like addition, subtraction, muliplication,  divition.\
            But in the field of algebra, the numbers are often represented by the symbols and are called variables. It also allows\
            the common formulation of the laws of arithmetic, and it is the first step that shows systematic exploration of all the\
            properties of a system of real numbers.",
        user = user1,
        category = category1
        )

session.add(item1)
session.commit()


item2 = Items(
        name = "Algebra 2 or Advanced Algebra",
        description = "This is the intermediate level Algebra or you can say prerequisite of Algebra 1.\
            This algebra has a high level of equations to solve as compared to pre-algebra.",
        user = user1,
        category = category1
        )

session.add(item2)
session.commit()


item3 = Items(
        name = "Abstract Algebra",
        description = "Abstract algebra is one of the divisions in algebra which discovers the truths relating to\
            algebraic systems independent of specific nature of some operations. These operations in specific cases have\
            certain properties. Thus we can conclude some consequences of such properties. Hence this branch of mathematics\
            called abstract algebra.",
        user = user1,
        category = category1
        )

session.add(item3)
session.commit()


item4 = Items(
        name = "Linear Algebra",
        description = "Linear algebra is a branch of algebra which applies to both applied as well as pure mathematics.\
            It deals with the linear mappings between the vector spaces. It also deals with the study of planes and lines.",
        user = user1,
        category = category1
        )

session.add(item4)
session.commit()


item5 = Items(
        name = "Commutative algebra",
        description = "Commutative algebra is one of the branches of algebra that studies the commutative rings and its ideals.\
            The algebraic number theory, as well as the algebraic geometry, depending on the commutative algebra.",
        user = user1,
        category = category1
        )

session.add(item5)
session.commit()



# Menu for Arithmetic
category2 = Categories(name = "Arithmetic")
session.add(category2)
session.commit()


item1 = Items(
        name = "Arithmetic operations",
        description = "The basic operations under arithmetic are addition and subtraction, division and multiplication\
            although the subject involves many other modified operations.",
        user = user1,
        category = category2
        )

session.add(item1)
session.commit()


item2 = Items(
        name = "Arithmetic Problems",
        description = "For example: The sum of two numbers is 50 and their difference is 30. Find the numbers",
        user = user1,
        category = category2
        )

session.add(item2)
session.commit()



# Menu for Geometry
category3 = Categories(name = "Geometry")
session.add(category3)
session.commit()

item1 = Items(
        name = "Algebraic Geometry",
        description = "is a branch of geometry studying zeros of multivariate polynomial. It includes linear and polynomial\
            algebraic equation used for solving about the sets of zeros.The application of this type includes Cryptography,\
            string theory, etc.",
        user = user1,
        category = category3
        )

session.add(item1)
session.commit()


item2 = Items(
        name = "Discrete Geometry",
        description = "is concerned with the relative position of simple geometric object, such as points, lines , triangles, circles etc.",
        user = user1,
        category = category3
        )

session.add(item2)
session.commit()


item3 = Items(
        name = "Differential Geometry",
        description = "uses techniques of algebra and calculus for problem-solving. The various problem include general\
            relativity in physics etc.",
        user = user1,
        category = category3
        )

session.add(item3)
session.commit()


item4 = Items(
        name = "Euclidean Geometry",
        description = "The study of plane and solid figures on the basis of axioms and theorems including points,\
            lines, planes, angles, congruence, similarity, solid figures. It has a wide range of application in Computer Science,\
            Modern Mathematics problem solving, Crystallography etc.",
        user = user1,
        category = category3
        )

session.add(item4)
session.commit()


item5 = Items(
        name = "Convex Geometry ",
        description = "includes convex shapes in Euclidean space using techniques of real analysis.\
            It has application in optimization and functional analysis in number theory.",
        user = user1,
        category = category3
        )

session.add(item5)
session.commit()


item6 = Items(
        name = "Topology",
        description = "is concerned with properties of space under continuous mapping. Its application includes\
            consideration of compactness, completeness, continuity, filters, function spaces, grills, clusters and bunches,\
            hyperspace topologies, initial and final structures, metric spaces, metrization, nets, proximal continuity,\
            proximity spaces, separation axioms, and uniform spaces.",
        user = user1,
        category = category3
        )

session.add(item6)
session.commit()



# Menu for Trigonometry

category4 = Categories(name = "Trigonometry")
session.add(category4)
session.commit()


item1 = Items(
        name = "Trigonometry Ratios-Sine, Cosine, Tangent",
        description = "The trigonometric ratios of a triangle are also called the trigonometric functions.\
            Sine, cosine, and tangent are 3 important trigonometric functions and are abbreviated as sin, cos,\
            and tan. Let us see how are these ratios or functions, evaluated in the case of a right-angled triangle.",
        user = user1,
        category = category4
        )

session.add(item1)
session.commit()


item2 = Items(
        name = "Trigonometry Angles",
        description = "The trigonometry angles which are commonly used in trigonometry problems.\
            The trigonometric ratios such as sine, cosine and tangent of these angles are easy to memorize. We will also show the\
            table where all the ratios and their respective angles values are mentioned. To find these angles we have to draw\
            a right-angled triangle, in which one of the acute angles will be the corresponding trigonometry angle.\
            These angles will be defined with respect to the ratio associated with it.",
        user = user1,
        category = category4
        )

session.add(item2)
session.commit()


item3 = Items(
        name = "Trigonometry Formula",
        description = "The Trigonometric formulas or Identities are the equations which are true in the case\
            of Right-Angled Triangles. Some of the special trigonometric identities",
        user = user1,
        category = category4
        )

session.add(item3)
session.commit()


item4 = Items(
        name = "Applications of Trigonometry",
        description = "Its applications is in various fields like oceanography, seismology, meteorology, physical sciences,\
            astronomy, acoustics, navigation, electronics, etc.",
        user = user1,
        category = category4
        )

session.add(item4)
session.commit()


item5 = Items(
        name = "Applications of Trigonometry in Real Life",
        description = "One of the most important real life applications of trigonometry is in the calculation of height\
            and distance. Some of the sectors where the concepts of trigonometry is extensively used are aviation department,\
            navigation, criminology, marine biology, etc.",
        user = user1,
        category = category4
        )

session.add(item5)
session.commit()

print "Items have been added"