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
    private var noTags: Array<String> = ["No Tags"]
    
    func fetchData() {
        db.collection("Restaurants").addSnapshotListener { (querySnapshot, error) in
            guard let documents = querySnapshot?.documents else {
                print("No documents")
                return
            }
            
            self.restaurants = documents.map { (queryDocumentSnapshot) -> Restaurant in
                let data = queryDocumentSnapshot.data()
                
                let name = data["name"] as? String ?? "No name"
                let rating = data["rating"] as? Double ?? 0
                let tag = data["tag"] as? Array<String> ?? self.noTags
                
                return Restaurant(name: name, rating: rating, tag: tag)
            }
        }
    }
 }
