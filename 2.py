import json

def main(element) :
    with open('test_payload.json') as file:
        content = json.load(file)
        for key, value in list(content.items()):            
            if(key == element):
                del content[key]
            else:
                if(type(content[key]).__name__ == 'dict'):
                    for subkey, subvalue in list(content[key].items()):
                        if(subkey == element):
                            del content[key][subkey]

    with open('demo.json', 'w') as file:
        json.dump(content, file, indent=4)

if __name__ == "__main__":
    main('outParams')