import yaml

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    with open("galagyguide.yaml", "w") as zfile:
        yaml.dump(hitchhikers, zfile)


if __name__ == "__main__":
    main()
