import {
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonContent,
    IonButton,
    IonSelect,
    IonSelectOption,
    IonItem,
    IonLabel,
    IonCheckbox,
    useIonAlert,
    IonRadioGroup,
    IonRadio,
} from "@ionic/react";
import React from "react";
import { BASE } from "../constants";

const Search: React.FC = () => {
    const [availabilities, setAvailabilities] = React.useState([]);
    const [availabilitiesState, setAvailabilitiesState] = React.useState(-1);
    // const [breeds, setBreeds] = React.useState([]);
    // const [breedsState, setBreedsState] = React.useState("");
    // const [dispositions, setDispositions] = React.useState([]);
    // const [dispositionsState, setDispositionsState] = React.useState("");
    // const [sizes, setSizes] = React.useState([]);
    // const [sizesState, setSizesState] = React.useState("");
    const [species, setSpecies] = React.useState([]);
    const [speciesState, setSpeciesState] = React.useState(-1);

    const [animalList, setAnimalList] = React.useState([]);

    const [presentAlert] = useIonAlert();

    const getOptions = async () => {
        const token = localStorage.getItem("token");
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
        };

        const response = await fetch(`${BASE}/animal-options/`, requestOptions);

        if (response.ok) {
            const data = await response.json();

            setAvailabilities(data.availabilities);
            setSpecies(data.species);
            console.log(data);
        } else {
            presentAlert({
                header: "Error",
                subHeader: "",
                message: "Unable to fetch filter options.",
                buttons: ["OK"],
            });
        }
    };

    const handleSubmit = async () => {
        //Options accepted by filter view: age, availability, availability_id, breed, breed_id, date_entered, disposition, id, image, name, news, shelter, shelter_id, size, size_id, species, species_id, views

        let url = `${BASE}/animals/?`;
        let urlSuffixes = [];

        console.log(availabilitiesState);

        if (availabilitiesState && availabilitiesState !== -1) {
            urlSuffixes.push(`availability=${availabilitiesState}`);
        }

        if (speciesState && speciesState !== -1) {
            urlSuffixes.push(`species=${speciesState}`);
        }

        url += urlSuffixes.join("&");

        console.log(url);

        const token = localStorage.getItem("token");
        const requestOptions = {
            method: "GET",
            headers: {
                Authorization: `Bearer ${token}`,
            },
        };

        const response = await fetch(url, requestOptions);

        if (response.ok) {
            const data = await response.json();
            console.log(data);
            setAnimalList(data);
        } else {
            presentAlert({
                header: "Error",
                subHeader: "",
                message: "Unable to get results.",
                buttons: ["OK"],
            });
        }
    };

    React.useEffect(() => {
        getOptions();
    }, []);

    return (
        <IonContent>
            <IonCard>
                <IonCardHeader>
                    <IonCardTitle>Search for matches</IonCardTitle>
                </IonCardHeader>
                <IonCardContent>
                    <div key="availability">
                        <h3>Availability</h3>
                        <IonRadioGroup
                            value={availabilitiesState}
                            allowEmptySelection={true}
                            onIonChange={(e) =>
                                setAvailabilitiesState(e.detail.value)
                            }
                        >
                            {availabilities.map((availability) => (
                                <IonItem>
                                    <IonLabel>
                                        {availability.availability}
                                    </IonLabel>
                                    <IonRadio
                                        slot="end"
                                        value={availability.id}
                                    />
                                </IonItem>
                            ))}
                        </IonRadioGroup>
                    </div>
                </IonCardContent>
                <IonCardContent>
                    <div key="species">
                        <h3>Species</h3>
                        <IonRadioGroup
                            value={speciesState}
                            allowEmptySelection={true}
                            onIonChange={(e) =>
                                setSpeciesState(e.detail.value)
                            }
                        >
                            {species.map((specie) => (
                                <IonItem>
                                    <IonLabel>{specie.name}</IonLabel>
                                    <IonRadio slot="end" value={specie.id} />
                                </IonItem>
                            ))}
                        </IonRadioGroup>
                    </div>
                </IonCardContent>
                <IonButton expand="block" onClick={handleSubmit}>
                    Find matches
                </IonButton>
            </IonCard>
            {animalList.map((animal) => (
                <IonCard>
                    <IonCardHeader>
                        <IonCardTitle>{animal.name}</IonCardTitle>
                    </IonCardHeader>
                    <IonCardContent>
                        {animal.image ? (
                            <IonCardContent>
                                <img width="100" height="100" src={animal.image} />
                            </IonCardContent>
                        ) : (
                            ``
                        )}

                        {animal.availability.availability ? (
                            <p>
                                Availability: {animal.availability.availability}
                            </p>
                        ) : (
                            ``
                        )}

                        {animal.species && animal.species.name ? (
                            <p>Species: {animal.species.name}</p>
                        ) : (
                            ``
                        )}

                        {animal.breed && animal.breed.name ? (
                            <p>Breed: {animal.breed.name}</p>
                        ) : (
                            ``
                        )}

                        {animal.disposition ? <p>Dispositions:</p> : ``}
                        <ul>
                            {animal.disposition.map((disposition) => (
                                <li>{disposition.disposition}</li>
                            ))}
                        </ul>

                        {animal.age ? <p>Age: {animal.age}</p> : ``}

                        {animal.size && animal.size.name ? (
                            <p>Size: {animal.size.name}</p>
                        ) : (
                            ``
                        )}
                    </IonCardContent>
                </IonCard>
            ))}
        </IonContent>
    );
};

export default Search;
