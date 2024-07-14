from nada_dsl import *

def nada_main():
    wizard = Party(name="Gandalf the Grey 🧙‍♂️")
    alien = Party(name="Zog from Planet X 🛸")

    secret_spell_power = SecretInteger(Input(name="wizard_spell_power", party=wizard))
    secret_alien_technology = SecretInteger(Input(name="alien_tech_level", party=alien))

    # Combining wizard's spell power and alien technology for a cosmic explosion
    cosmic_explosion = (secret_spell_power ** 3) + (secret_alien_technology * 42)

    # A second transformation involving a mythical creature
    phoenix = Party(name="Fawkes the Phoenix 🔥")
    secret_phoenix_feathers = SecretInteger(Input(name="phoenix_feathers", party=phoenix))

    # The phoenix feathers multiply the cosmic explosion to create a supernova
    supernova = cosmic_explosion * secret_phoenix_feathers

    # The final output is the supernova value, a cosmic spectacle
    return [Output(supernova, "supernova_output", wizard)]

