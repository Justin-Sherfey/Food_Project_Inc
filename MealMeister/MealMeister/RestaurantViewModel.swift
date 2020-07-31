//
//  RestaurantViewModel.swift
//  MealMeister
//
//  Created by Brett Beattie on 7/29/20.
//  Copyright © 2020 Andrew Thomas. All rights reserved.
//

import Foundation
import Firebase

class RestaurantViewModel: ObservableObject {
    @Published var restaurants = [Restaurant]()
    
    private var db = Firestore.firestore()
    
    func fetchData() {
        db.collection("Restaurants").addSnapshotListener { (querySnapshot, error) in
            guard let documents = querySnapshot?.documents else {
                print("No documents")
                return
            }
            
            self.restaurants = documents.map { (queryDocumentSnapshot) -> Restaurant in
                let data = queryDocumentSnapshot.data()
                
                let displayName = data["displayName"] as? String ?? ""
                let name = data["name"] as? String ?? ""
                let tag = data["tag"] as? String ?? ""
                
                return Restaurant(displayName: displayName, name: name, tag: tag)
            }
        }
    }
 }
