NB_SIÈGES = 20
nb_sièges_libres = 0
nb_sièges_à_réserver = ''

# Entrées.
nb_sièges_réservation = int(input())

for i in range( 1, NB_SIÈGES + 1 ):
    état_siège = int( input() )
    if nb_sièges_libres < nb_sièges_réservation:
        if état_siège == 0:
            print(i)
            nb_sièges_libres += 1
        # end if
    # end if
    i += 1
# end for
