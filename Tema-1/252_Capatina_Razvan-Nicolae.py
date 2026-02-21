import numpy as np
import matplotlib.pyplot as plt

# Choose number of chords to draw in the simulation:
num_chords = 10000


def draw_circle_and_triangle(ax):
    circle = plt.Circle((0, 0), 1, color='w', linewidth=2, fill=False)
    ax.add_patch(circle)  # Draw circle
    ax.plot([np.cos(np.pi / 2), np.cos(7 * np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(np.pi / 2), np.cos(- np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(- np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(- np.pi / 6), np.cos(7 * np.pi / 6)],
            [np.sin(- np.pi / 6), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    plt.show()


def bertrand_simulation(method_number):
    # Simulation initialisation parameters
    count = 0

    # Figure initialisation
    plt.style.use('dark_background')  # use dark background
    ax = plt.gca()
    ax.cla()  # clear things for fresh plot
    ax.set_aspect('equal', 'box')
    ax.set_xlim((-1, 1))  # Set x axis limits
    ax.set_ylim((-1, 1))  # Set y axis limits

    # Repeat the following simulation num_chords times:

    # Step 1: Construct chord according to chosen method
    for k in range(1, num_chords + 1):
        x, y = bertrand_methods[method_number]()

        # Step 2: Compute length of chord and compare it with triangle side sqrt(3)
        length = np.sqrt((x[0] - x[1]) * (x[0] - x[1]) + (y[0] - y[1]) * (y[0] - y[1]))
        count += (length > np.sqrt(3))
        print("Probability = {:.4f}".format(count / k))  # Display probability after each simulation
        if k <= 1000:  # only plot the first 1000 chords
            if length > np.sqrt(3):
                plt.plot(x, y, color='y', alpha=0.1)
            else:
                plt.plot(x, y, color='m', alpha=0.1)

    draw_circle_and_triangle(plt.gca())
    plt.show()


def bertrand1():

    """
    Varianta 1, probabilitate 33,(3)%
    """

    """Generate random chords and midpoints using "Method 1".

    Pairs of (uniformly-distributed) random points on the unit circle are
    selected and joined as chords.

    """

    theta1 = np.random.random() * 2 * np.pi
    theta2 = np.random.random() * 2 * np.pi

    x = np.cos([theta1, theta2]);
    y = np.sin([theta1, theta2]);

    return x, y

def bertrand2():

    """
    Varianta 2, probabilitate 25%
    """

    """
    -generez un punct aleator in interiorul cercului care va fi considerat mijlocul corzii;
    -se poate demonstra ca acea coarda e perpendiculara pe dreapta ce uneste mijlocul ei cu centrul cercului;
    -aflu ecuatia dreptei ce uneste mijlocul corzii si centrul cercului (cu determinantul de 3x3 egal cu 0, de exemplu);
    -gasesc ecuatia dreptei perpendiculare pe dreapta aceasta, stiind faptul ca
    panta dreapta * panta perpendiculara dreapta = -1;
    -apoi fac sistem de ecuatii intre ecuatia perpendicularei (adica a corzii cautate) si ecuatia cercului
    si identific capetele corzii;
    """

    x0 = np.random.random() * 2 - 1
    y0 = np.random.random() * 2 - 1

    while (x0 * x0 + y0 * y0 >= 1 or x0 == 0 or y0 == 0):
        x0 = np.random.random() * 2 - 1
        y0 = np.random.random() * 2 - 1

    m = -x0 / y0 #panta dreptei ce uneste mijlocul de centrul cercului este y0 / x0, deci panta corzii cautate este -x0 / y0 (m)
    #de asemenea, din ecuatia dreptei y = mx + c, avem c = 0 pentru dreapta ce uneste centrul cercului de mijloc,
    #pentru ca trece prin (0, 0) (centru)
    c = (x0 * x0 + y0 * y0) / y0 #in schimb, pentru ecuatia corzii, c-ul din y = mx + c este nenul si
    #egal cu (x0 * x0 + y0 * y0) / y0

    #aici am facut sistem de ecuatii cu ecuatia cercului de raza 1 si rezolv ecuatia de gradul 2 folosind A, B, C si delta

    A = m * m + 1
    B = 2 * m * c
    C = c * c - 1

    delta = B * B - 4 * A * C

    x1 = (-B + np.sqrt(delta)) / (2 * A)
    x2 = (-B - np.sqrt(delta)) / (2 * A)

    #am gasit abscisele celor 2 puncte, acum introduc valorile in ecuatia corzii(coardei?) si gasesc ordonatele

    y1 = m * x1 + c
    y2 = m * x2 + c

    return [x1, x2], [y1, y2] #acestea sunt intersectiile corzii cu circumferinta cercului


def bertrand3():

    """
    Varianta 3, probabilitate 50%
    """

    #generez punct aleator pe circumferinta cercului
    x = np.random.random() * 2 - 1 #x va fi astfel intre [-1; 1]
    y = np.sqrt(1 - x * x)
    #pentru un x fixat, exista cel mult 2 de y care satisfac ecuatia cercului, le dau probabilitate de 50% amandurora
    #de a fi luati
    if np.random.random() >= 0.5:
        y = -y

    #am un punct aleator pe cerc si centrul cercului (0, 0)
    #generez un punct aleator pe aceasta raza, care sa fie intre centrul cercului si punctul aleator de pe circumferinta
    rand = np.random.random()
    x0 = x * rand + 0 * (1 - rand)
    y0 = y * rand + 0 * (1 - rand)
    #nu mai era nevoie de 0 * (1 - rand), dar am scris formula mai generala (daca centrul era la coordonate (a, b) arbitrare)
    while y0 == 0:
        rand = np.random.random()
        x0 = x * rand + 0 * (1 - rand)
        y0 = y * rand + 0 * (1 - rand)

    #(x0, y0) este acum mijlocul corzii
    #de aici in continuare aplic acelasi algoritm ca la bertrand2

    m = -x0 / y0

    c = (x0 * x0 + y0 * y0) / y0

    A = m * m + 1
    B = 2 * m * c
    C = c * c - 1

    delta = B * B - 4 * A * C

    x1 = (-B + np.sqrt(delta)) / (2 * A)
    x2 = (-B - np.sqrt(delta)) / (2 * A)

    y1 = m * x1 + c
    y2 = m * x2 + c

    return [x1, x2], [y1, y2]


bertrand_methods = {1: bertrand1, 2: bertrand2, 3: bertrand3}

method_choice = int(input('Choose method to simulate: '))
bertrand_simulation(method_choice)
